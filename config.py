# configurations
import sys


# generate default configuration given necessary infos and hyperparameters
def gen_default(dataset, n_class, size, mean, std, batch_size=1, lr=1e-4,
                epoch=150):
    default = {
        'root': './data/' + dataset,
        'n_class': n_class,
        'size': size,
        'mean': mean,
        'std': std,
        'batch_size': batch_size,
        'optimizer': 'Adam',
        'lr': lr,
        'epoch': epoch,
        'aug': False
    }
    return default


config = {
    'uhcs': {
        'default': gen_default('uhcs', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'uhcs-fold-0': {
        'default': gen_default('uhcs-fold-0', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'uhcs-fold-1': {
        'default': gen_default('uhcs-fold-1', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'uhcs-fold-2': {
        'default': gen_default('uhcs-fold-2', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'uhcs-fold-3': {
        'default': gen_default('uhcs-fold-3', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'uhcs-fold-4': {
        'default': gen_default('uhcs-fold-4', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'uhcs-fold-5': {
        'default': gen_default('uhcs-fold-5', n_class=4, size=(484, 645),
                               mean=[0.449, 0.449, 0.449], std=[0.168, 0.168, 0.168]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'tomography': {
        'default': gen_default('tomography', n_class=2, size=(852, 852),
                               mean=[0.504, 0.504, 0.504], std=[0.051, 0.051, 0.051]),
        'v1': {'model': 'pixelnet'},
        'v2': {'model': 'unet'},
        'v3': {'model': 'segnet', 'optimizer': 'SGD', 'lr': 0.01},
        'v4': {'model': 'pixelnet', 'aug': True},
        'v5': {'model': 'unet', 'aug': True},
        'v6': {'model': 'segnet', 'aug': True, 'optimizer': 'SGD', 'lr': 0.01}
    },
    'tomography224': {
        'default': gen_default('tomography224', n_class=2, size=(852, 852),
                               mean=[0.504, 0.504, 0.504], std=[0.051, 0.051, 0.051]),
        'v1': {'model': 'segnet', 'aug': True, 'batch_size': 16}
    }
}


# combine the default config with version config
def get_config(dataset, version):
    try:
        args = config[dataset]['default'].copy()
    except KeyError:
        print('dataset %s does not exist' % dataset)
        sys.exit(1)
    try:
        args.update(config[dataset][version])
    except KeyError:
        print('version %s is not defined' % version)
    args['name'] = dataset + '_' + version
    return args
