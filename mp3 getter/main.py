import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QDialog, QRadioButton, QHBoxLayout, QDialogButtonBox
from pytube import YouTube
from youtubesearchpython import VideosSearch

class StartScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Action buttons
        download_individually_button = QPushButton("Download Individually", self)
        download_top_10_button = QPushButton("Download Top 10", self)
        sync_button = QPushButton("Sync", self)
        dev_button = QPushButton("Dev", self)

        # Connect buttons to corresponding actions
        download_individually_button.clicked.connect(self.open_download_individually)
        download_top_10_button.clicked.connect(self.open_download_top_10)
        sync_button.clicked.connect(self.open_sync)
        dev_button.clicked.connect(self.open_dev)

        layout.addWidget(download_individually_button)
        layout.addWidget(download_top_10_button)
        layout.addWidget(sync_button)
        layout.addWidget(dev_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Start Screen')

    def open_download_individually(self):
        self.hide()
        download_individually_dialog = DownloadIndividuallyDialog()
        download_individually_dialog.exec_()
        self.show()

    def open_download_top_10(self):
        self.hide()
        download_top_10_dialog = DownloadTop10Dialog()
        download_top_10_dialog.exec_()
        self.show()

    def open_sync(self):
        self.hide()
        sync_dialog = SyncDialog()
        sync_dialog.exec_()
        self.show()

    def open_dev(self):
        self.hide()
        dev_dialog = DevDialog()
        dev_dialog.exec_()
        self.show()


class DownloadIndividuallyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.file_path = ""
        self.artist = ""
        self.song = ""
        self.youtube_search_term = ""
        self.output_folder = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Choose source (Spotify or YouTube)
        source_label = QLabel("Choose source:")
        self.spotify_radio = QRadioButton("Spotify", self)
        self.youtube_radio = QRadioButton("YouTube", self)
        self.spotify_radio.setChecked(True)  # Default to Spotify
        self.spotify_radio.toggled.connect(self.toggle_input_fields)
        self.youtube_radio.toggled.connect(self.toggle_input_fields)

        layout.addWidget(source_label)
        layout.addWidget(self.spotify_radio)
        layout.addWidget(self.youtube_radio)

        # Spotify input fields
        self.artist_label = QLabel("Enter Artist:")
        self.artist_line_edit = QLineEdit(self)
        self.song_label = QLabel("Enter Song:")
        self.song_line_edit = QLineEdit(self)

        layout.addWidget(self.artist_label)
        layout.addWidget(self.artist_line_edit)
        layout.addWidget(self.song_label)
        layout.addWidget(self.song_line_edit)

        # YouTube input fields
        self.youtube_label = QLabel("Enter YouTube Search Term:")
        self.youtube_line_edit = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.show_youtube_search_result)

        layout.addWidget(self.youtube_label)
        layout.addWidget(self.youtube_line_edit)
        layout.addWidget(self.search_button)

        # Output folder selection
        output_folder_label = QLabel("Select Output Folder:")
        self.output_folder_line_edit = QLineEdit(self)
        output_folder_button = QPushButton("Browse", self)
        output_folder_button.clicked.connect(self.browse_output_folder)

        layout.addWidget(output_folder_label)
        layout.addWidget(self.output_folder_line_edit)
        layout.addWidget(output_folder_button)

        # Action button
        action_button = QPushButton("Download", self)
        action_button.clicked.connect(self.perform_action)

        layout.addWidget(action_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Download Individually Dialog')

    def toggle_input_fields(self):
        spotify_checked = self.spotify_radio.isChecked()
        self.artist_label.setVisible(spotify_checked)
        self.artist_line_edit.setVisible(spotify_checked)
        self.song_label.setVisible(spotify_checked)
        self.song_line_edit.setVisible(spotify_checked)

        youtube_checked = self.youtube_radio.isChecked()
        self.youtube_label.setVisible(youtube_checked)
        self.youtube_line_edit.setVisible(youtube_checked)
        self.search_button.setVisible(youtube_checked)

    def show_youtube_search_result(self):
        # Simulate the YouTube search result (replace with actual logic)
        youtube_title = "Sample YouTube Title"
        result_dialog = YoutubeSearchResultDialog(youtube_title, self)
        result_dialog.exec_()

    def browse_output_folder(self):
        folder_dialog = FolderBrowserDialog(self)
        folder_dialog.exec_()
        if folder_dialog.result() == QDialog.Accepted:
            self.output_folder = folder_dialog.selected_folder
            self.output_folder_line_edit.setText(self.output_folder)

    def perform_action(self):
        if self.spotify_radio.isChecked():
            self.artist = self.artist_line_edit.text()
            self.song = self.song_line_edit.text()
            # Perform Spotify download action here
            print("Spotify Download - Artist:", self.artist)
            print("Spotify Download - Song:", self.song)
        elif self.youtube_radio.isChecked():
            self.youtube_search_term = self.youtube_line_edit.text()
            # Perform YouTube download action here
            print("YouTube Download - Search Term:", self.youtube_search_term)
            search_query = self.youtube_search_term
            video_url = VideosSearch(search_query, limit=1).result()['result'][0]['link']
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            mp3_filename = f"{artist_name} - {song_name}.mp3"
            print("Filename: ", mp3_filename)
            if input("Wanna change (y/n)? ") == "y":
                mp3_filename = input("New Filename: ")
            mp3_filepath = os.path.join(output_path, mp3_filename)
            audio_stream.download(output_path=output_path, filename=mp3_filename)
            ctmp3.process_file(mp3_filepath)
        # Perform common action for both sources (e.g., save to output folder)
        print("Output Folder:", self.output_folder)
        # Close the dialog
        self.accept()


class YoutubeSearchResultDialog(QDialog):
    def __init__(self, youtube_title, parent=None):
        super().__init__(parent)

        self.youtube_title = youtube_title

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("YouTube Search Result:")
        result_label = QLabel(self.youtube_title)

        layout.addWidget(title_label)
        layout.addWidget(result_label)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)

        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle('YouTube Search Result')


class FolderBrowserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.selected_folder = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        folder_label = QLabel("Select Folder:")
        self.folder_line_edit = QLineEdit(self)

        layout.addWidget(folder_label)
        layout.addWidget(self.folder_line_edit)

        browse_button = QPushButton("Browse", self)
        browse_button.clicked.connect(self.browse_folder)

        layout.addWidget(browse_button)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)

        self.setLayout(layout)
        self.setWindowTitle('Folder Browser Dialog')

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.selected_folder = folder_path
            self.folder_line_edit.setText(self.selected_folder)


class DownloadTop10Dialog(QDialog):
    # Implement the DownloadTop10Dialog as needed
    pass


class SyncDialog(QDialog):
    # Implement the SyncDialog as needed
    pass


class DevDialog(QDialog):
    # Implement the DevDialog as needed
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_screen = StartScreen()
    start_screen.show()
    sys.exit(app.exec_())
