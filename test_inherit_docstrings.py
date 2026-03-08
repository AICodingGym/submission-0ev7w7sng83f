import sys
sys.path.insert(0, '/home/simon/workspace/aicodinggym/astropy-7166')

# 直接从源代码导入，跳过 astropy.__init__ 的检查
from astropy.utils.misc import InheritDocstrings


class BaseClass(metaclass=InheritDocstrings):
    """Base class docstring."""
    
    @property
    def my_property(self):
        """This is a property docstring."""
        return self._value
    
    def my_method(self):
        """This is a method docstring."""
        pass


class DerivedClass(BaseClass):
    """Derived class docstring."""
    pass


# 测试
if __name__ == '__main__':
    # 检查方法文档字符串继承
    assert DerivedClass.my_method.__doc__ == "This is a method docstring."
    print("✓ Method docstring inherited successfully")
    
    # 检查属性文档字符串继承（这是修复的关键）
    base_property = getattr(BaseClass, 'my_property')
    derived_property = getattr(DerivedClass, 'my_property')
    
    print(f"Base property __doc__: {base_property.__doc__}")
    print(f"Derived property __doc__: {derived_property.__doc__}")
    
    assert derived_property.__doc__ == "This is a property docstring."
    print("✓ Property docstring inherited successfully")
    
    print("\n✓ All tests passed! InheritDocstrings now works for properties.")