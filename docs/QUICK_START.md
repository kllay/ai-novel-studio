# 🚀 快速开始指南

## 5 分钟内启动项目

### 前置检查
- [ ] Docker 已安装
- [ ] Docker Compose 已安装
- [ ] 至少 20GB 磁盘空间
- [ ] 20GB+ 可用内存

### 启动步骤

```bash
# 1. 克隆项目
git clone https://github.com/kllay/ai-novel-studio.git
cd ai-novel-studio

# 2. 启动所有服务
cd backend
docker-compose up -d

# 3. 等待 1-2 分钟，然后访问
# 前端: http://localhost:5173
# API: http://localhost:8000/docs
```

## 常见问题

### Q: 容器启动失败？
A: 检查 Docker 是否正常运行，查看日志: `docker-compose logs`

### Q: 如何停止服务？
A: `docker-compose down`
