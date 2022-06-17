from detecto import core, utils, visualize

dataset = core.Dataset('images/')
model = core.Model(['bsW', 'bsH'])

model.fit(dataset)