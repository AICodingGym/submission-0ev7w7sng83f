import inspect

# 直接复制修复后的 InheritDocstrings 元类代码
class InheritDocstrings(type):
    """Metaclass that inherits docstrings from base classes."""
    
    def __new__(cls, name, bases, dct):
        for base in bases:
            for attr_name in dir(base):
                if not attr_name.startswith('_'):
                    base_member = getattr(base, attr_name)
                    # 修复：检查函数或属性
                    if inspect.isfunction(base_member) or isinstance(base_member, property):
                        if attr_name not in dct:
                            dct[attr_name] = base_member
                        elif not dct[attr_name].__doc__:
                            dct[attr_name].__doc__ = base_member.__doc__
        return super().__new__(cls, name, bases, dct)


# 创建测试类
class BaseClass(metaclass=InheritDocstrings):
    """Base class."""
    
    @property
    def my_property(self):
        """Property docstring."""
        return 42


class DerivedClass(BaseClass):
    """Derived class."""
    pass


# 测试
print("Base property __doc__:", BaseClass.my_property.__doc__)
print("Derived property __doc__:", DerivedClass.my_property.__doc__)

if DerivedClass.my_property.__doc__ == "Property docstring.":
    print("✓ 测试通过！属性文档字符串成功继承")
else:
    print("✗ 测试失败")