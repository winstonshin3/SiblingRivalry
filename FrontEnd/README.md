# Sibling Rivalry FE

## ToC

- [Develop Environment](#develop-environment)
- [Run the Application](#run-the-application)
- [Application Archtecture](#application-archtecture)

## Develop Environment

| Tool            | Version     | installation                  |
| --------------- | ----------- | ----------------------------- |
| Node JS         | 20.12.2     | [link](https://nodejs.org/en) |
| Package Manager | Yarn or npm | see below                     |
| REACT JS        | 18.2.0      | [goto](#run-application)      |
| Build Tool      | vite-5.4.1  |                               |

> `npm` is automatically installed with `node js`. To make sure `Node JS` and `npm` is installed correctly, type commands below and see if versions of each programs printed.

```
node -v
npm -v
```

> `yarn` isn't really necessary for this project, but in purpose of `speed` and `security`, I recommand to use `yarn` instead of `npm` [link](https://medium.com/@salluarsh/npm-vs-yarn-f4a7331442b7). If you`re going to use yarn as a package manager, you have to install it [link](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable)

```
npm install --global yarn
```

## Run the Application

Open terminal on this Directory. And...

1. install depengencies

```
npm install
# or
yarn
```

> Make sure to All depengencies are installed without an error. Installed depengencies are placed in `./node_modules` directory

2. run dev server

```
npm run dev
# or
yarn dev
```

> Open http://localhost:5173 or url that printed on console after dev server is successfully hosted

## Application Archtecture

> FSD(Feature Sliced Design) [link](https://feature-sliced.design)
