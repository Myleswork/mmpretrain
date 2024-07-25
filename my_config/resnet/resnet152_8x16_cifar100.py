_base_ = [
    '../_base_/models/resnet152_cifar.py',
    '../_base_/datasets/cifar100_bs16.py',
    '../_base_/schedules/cifar10_bs512.py',
    '../_base_/default_runtime.py'
]

# model settings
model = dict(head=dict(num_classes=100))

# schedule settings
optim_wrapper = dict(optimizer=dict(weight_decay=0.0005))

param_scheduler = dict(
    type='MultiStepLR',
    by_epoch=True,
    milestones=[60, 120, 160],
    gamma=0.2,
)
