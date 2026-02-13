class DefaultValue:
    def __init__(fx,name='Faysal',age=2):
        fx.name=name
        fx.age=age
    def output(x):
        print(f"name: {x.name} ; age: {x.age}")

obj=DefaultValue()
obj.output()

obj_1=DefaultValue('Ovi',27)
obj_1.output()