# 接口规则说明

## 1 用户

### 获取当前IP地址
```
返回：
{"ip":"127.0.0.1"}
```

### 验证用户名和密码

```
POST: {name:name, password:password}
返回：
正确: HTTP200
错误: {"error":error}
```

### 获取当前登陆用户
```
返回:
已登陆: {"id":1,"name":"test"}
错误: {"error":error}
```

## 2 网盘

### 获取当前路径下的文件
```
POST: {path:path}
返回:
{"dirs":[{"id":1,"name":"dir1"}, {"id":2,"name":"dir2"},...],"files":[{"id":1,"name":"file1"}, {"id":2,"name":"file2"},...]}
```
### 重命名文件夹
```
POST:{id:id}
```

### 重命名文件
```
POST:{id:id}
```

### 上传文件
```
POST:{path:path, name:name}
```

### 新建文件夹
```
POST:{path:path, name:name}
```

### 下载文件
```
POST:{files:[file1, file2, ...]}
返回:
{"url":"url"}
```

## 3 帐套

### 获取帐套列表树
```
返回:
[{"id":1,"name":"2014","children":[{"id":2,"name":"客户","children":[{"id":3,"name":"aaa表","children":[]},{"id":4,"name":"bbb表","children":[]}]},{"id":5,"name":"富锐泰","children":[{"id":6,"name":"aaa表","children":[]},{"id":7,"name":"bbb表","children":[]}]},{"id":8,"name":"供应商","children":[{"id":9,"name":"aaa表","children":[]},{"id":10,"name":"bbb表","children":[]}]}]},{"id":11,"name":"2015","children":[{"id":12,"name":"客户","children":[{"id":13,"name":"aaa表","children":[]},{"id":14,"name":"bbb表","children":[]}]},{"id":15,"name":"富锐泰","children":[{"id":16,"name":"aaa表","children":[]},{"id":17,"name":"bbb表","children":[]}]},{"id":18,"name":"供应商","children":[{"id":19,"name":"aaa表","children":[]},{"id":20,"name":"bbb表","children":[]}]}]},{"id":21,"name":"2016","children":[{"id":22,"name":"客户","children":[{"id":23,"name":"aaa表","children":[]},{"id":24,"name":"bbb表","children":[]}]},{"id":25,"name":"富锐泰","children":[{"id":26,"name":"aaa表","children":[]},{"id":27,"name":"bbb表","children":[]}]},{"id":28,"name":"供应商","children":[{"id":29,"name":"aaa表","children":[]},{"id":30,"name":"bbb表","children":[]}]}]}]
```


### 获取帐套数据
```
POST:{id:id}
返回:
{
	"page":1,
	"totalPage":100,
	"field":["col1", "col2", "col3"],
	"data":[
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3},
		{"col1":1, "col2":2, "col3":3}
	]
}
```

### 插入数据
```
POST:{tableId:id, data:{col1:xxx, col2:xxx, ...}}
```

### 删除数据
```
POST:{tableId:tableId, rowid: rowid}
```

### 添加列
```
POST:{tableId: tableId, colName: name, dataType: "Number|string", defaultValue: value}
```

### 删除列
```
POST:{tableId: tableId, colName: name}
```

### 修改数据
```
POST:{tableId:tableId, rowId:rowId, col:colName}
```
