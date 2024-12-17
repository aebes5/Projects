# Build stage
FROM node:18 AS build

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy application source code
COPY . .

# Build the Vite app
RUN npm run build

# Debug to check if the dist folder exists
RUN ls -la /app/dist

# Serve stage
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
