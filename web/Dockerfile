
FROM node:14-alpine 


# Add a work directory
WORKDIR /code/src
# Cache and Install dependencies
COPY package.json .


RUN npm install

# Copy app files
COPY . .
# Start the app
CMD [ "npm", "start" ]
