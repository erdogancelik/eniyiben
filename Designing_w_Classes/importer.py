import importlib

def call_it(modname):
    return importlib.import_module(modname)

if __name__ == '__main__':
    module = call_it('foo')
    module.main()