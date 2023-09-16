# 项目名称

欢迎来到项目名称！本文将指导您设置和运行项目的过程。

## 先决条件

在开始之前，请确保您的系统上已安装以下先决条件：

- Python 3.x
- Virtualenv（可选，但建议使用）
- pip（Python包管理器）

## 设置


1. **克隆项目存储库**：
   ```bash
   git clone https://github.com/xxx/xxx.git
    ```

2. **导航到项目目录**：
    ```bash
    cd dj_test
    ```
   
3. **创建虚拟环境**（可选，但建议使用）：
    ```bash
    python -m venv venv
    ```
   

4. **激活虚拟环境**：

- 在Windows上：

  ```
  venv\Scripts\activate
  ```

- 在macOS和Linux上：

  ```
  source venv/bin/activate
  ```

5. **安装项目依赖项**：
    ```bash
    pip install -r requirements.txt 
    ```
   

6. **配置数据库**：
    ```bash
    python manage.py makemigrations
    python manage.py migrate     
    ```


## 运行项目

1. **要在本地运行项目，请使用以下命令**：
    ```bash
    python manage.py runserver
    ```

2. **加载初始数据**:

    ```bash
    python manage.py loaddata data.json
    ```

# 笔试题


1.**使用原生sql获取产品名称和其所属的分类名称，假设产品ID为1**

项目运行后访问：
```http request
    http://localhost:8080/product/1
```

2.**实现产品列表API,返回数据格式如下**：
```json
    [
        {'id': 1,
         'name': 'product 1',
         'category': {'id': 1, 'name': 'category1'}
        },
        {'id': 2,
         'name': 'product 2',
         'category': {'id': 1, 'name': 'category1'}
        },
        {'id': 3,
         'name': 'product 3',
         'category': {'id': 2, 'name': 'category2'}
        }
        ...
    ]
```

通过 django + drf（尽量使用）或者django实现该API。


项目运行后访问：
```http request
    http://localhost:8080/products
```



