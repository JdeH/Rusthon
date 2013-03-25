def create_object():
    object = JSObject()
    object.__class__ = klass
    object.__dict__ = JSObject()

    init = get_attribute(object, '__init__')
    if init:
        init.apply(None, arguments)
    return object


def create_class(class_name, parents, attrs):
    klass = JSObject()
    klass.bases = parents
    klass.__name__ = class_name
    klass.__dict__ = attrs

    def __call__():
        args = arguments.___insert(0, klass)
        return create_object.apply(None, args)
    klass.__call__ = create_object
    return klass


def get_attribute(object, attribute):
    if attribute == '__call__':
        if JS('_.isFunction(object)'):
            return object
    attr = JS("object[attribute]")
    if attr:
        return attr
    __dict__ = object.__dict__
    if __dict__:
        attr = get_attribute(__dict__, attribute)
        if attr:
            return attr
    __class__ = object.__class__
    if __class__:
        __dict__ = __class__.__dict__
        attr = __dict__.___get(attribute)
        if attr:
            if JS('_.isFunction(attr)'):
                def method():
                    o = arguments.___insert(0, object)
                    r = attr.apply(None, arguments)
                    return r
                return method
            return attr
        bases = __class__.bases
        for i in range(bases.length):
            base = bases.___get(i)
            attr = get_attribute(base, attribute)
            if attr:
                return attr
    return None


def set_attribute(object, attr, value):
    __dict__ = object.__dict__
    __dict__.___set(attr, value)


def get_arguments(parameters, args, kwargs):
    out = JSObject()
    if parameters.args.length:
        argslength = parameters.args.length
    else:
        argslength = 0
    kwargslength = JS('Object.keys(parameters.kwargs).length')
    j = 0
    for i in argslength:
        arg = JS('parameters.args[j]')
        if kwargs:
            kwarg = JS('kwargs[arg]')
            if kwarg:
                JS('out[arg] = kwarg')
                JS('delete kwargs[arg]')
            else:
                JS('out[arg] = args[j]')
                j = j + 1
        else:
            JS('out[arg] = args[j]')
            j = j + 1
    args = args.slice(j)
    if parameters.vararg:
        JS("out[parameters.vararg] = args")
    if parameters.varkwarg:
        JS("out[parameters.varkwarg] = kwargs")
    return out
