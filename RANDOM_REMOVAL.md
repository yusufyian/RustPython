# Python random库支持移除说明

本文档记录了从RustPython项目中移除Python random库支持所做的更改。

## 移除的文件

### Rust实现层面
- `stdlib/src/random.rs` - random模块的Rust实现
  
### Python标准库层面  
- `Lib/random.py` - Python层面的random模块实现

### 测试文件
- `extra_tests/snippets/stdlib_random.py` - random库的测试用例
- `Lib/test/test_random.py` - 标准库测试文件

## 修改的文件

### 模块注册
- `stdlib/src/lib.rs`:
  - 移除了 `mod random;` 声明
  - 从 `get_module_inits()` 函数中移除了 `"_random" => random::make_module`

### 依赖配置
- `stdlib/Cargo.toml`:
  - 移除了 `mt19937 = "3.1"` 依赖

## 影响和注意事项

### 1. 直接影响
- `import random` 将会失败，抛出 `ModuleNotFoundError`
- 所有依赖random模块的Python代码将无法运行

### 2. 仍然可用的功能
- `os.urandom()` - 操作系统级别的随机数生成仍然可用
- `hashlib` 等其他加密相关模块不受影响
- 哈希种子功能仍然正常工作（通过 `PYTHONHASHSEED` 环境变量或 `-R` 选项）

### 3. 受影响的标准库模块
以下模块可能会因为缺少random而无法正常工作：
- `tempfile.py` - 临时文件名生成
- `uuid.py` - UUID生成的部分功能  
- `statistics.py` - 统计模块的采样功能
- `email/` 模块 - 邮件边界生成

### 4. 受影响的测试
大量测试文件依赖random模块，移除后这些测试将无法运行：
- `test_math.py`
- `test_builtin.py` 
- `test_float.py`
- 以及其他约50+个测试文件

## 恢复方法

如果需要恢复random库支持，需要：

1. 恢复被删除的文件
2. 在 `stdlib/src/lib.rs` 中重新添加模块声明和注册
3. 在 `stdlib/Cargo.toml` 中重新添加 `mt19937` 依赖
4. 重新编译项目

## 替代方案

如果仍需要随机数功能，可以考虑：

1. 使用 `os.urandom()` 获取密码学强度的随机字节
2. 实现简单的线性同余生成器
3. 使用外部的随机数库
4. 手动实现特定需要的随机数算法

## 编译验证

执行以下命令验证移除成功：
```bash
cargo check --package rustpython-stdlib
```

应该能够成功编译而不出现与random相关的错误。 