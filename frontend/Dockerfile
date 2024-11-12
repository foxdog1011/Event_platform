# 第一步：构建前端应用
FROM node:16 as build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# 第二步：使用 Nginx 服务构建的应用
FROM nginx:latest

# 删除默认配置文件
RUN rm /etc/nginx/conf.d/default.conf

# 复制自定义的 Nginx 配置文件
COPY nginx.conf /etc/nginx/conf.d

# 复制构建的前端文件到 Nginx 默认的静态文件目录
COPY --from=build /app/build /usr/share/nginx/html

# 暴露端口（与 docker-compose 中的端口一致）
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
