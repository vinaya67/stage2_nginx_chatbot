FROM node:18

WORKDIR /app
COPY package.json tsconfig.json ./
COPY src ./src

RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
