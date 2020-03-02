FROM node:stretch-slim as build-stage
WORKDIR /app
COPY package.json yarn.lock /app/
RUN yarn
COPY . /app
RUN yarn build

FROM nginx:stable-alpine as production-stage
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist /app
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]