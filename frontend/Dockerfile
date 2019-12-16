FROM nginx:stable-alpine as production-stage
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY dist /app
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]