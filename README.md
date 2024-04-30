tabby
=====

Tabby is a lightweight, self-hosted dashboard specifically designed for
displaying multiple web services in tabs using iframes.

It requires minimal setup and provides a simple way to access your services from
a single page with tabs.

> [!CAUTION]
> Tabby is just a little side project at the moment. I created it to solve my
> my specific use case. I'm open to MRs and forks, but ultimately this project
> is not a priority of mine.
> That said, I'd appreciate if you would share any improvements or
> modifications.

Features
===
- Load tab configurations from YAML files
- Group tabs into groups
- Toggle visibility of inactive tab groups
- Dark mode for better readability

Configuration
===
Tabby is configured using YAML files. You can create a `config` directory in
the root of the project and place your configuration files there. Tabby will
load all the files in the `config` directory, so you can split your tabs into
multiple files.

Example configuration:
```yaml
tabGroupA:
  - name: SomeApp
    url: http://something:8080
  - name: SomeOtherApp
    url: http://something:8081
tabGroupB:
  - name: SomeThing
    url: http://something:8083
  - name: SomeAppThing
    url: http://something:8084
```

Running with docker compose
===

You'll need to pick the port you want to run Tabby on. Internally, Tabby runs on
port 5000, but you can map it to any port you want.

```yaml
version: '3.7'
services:
  tabby:
    image: ghcr.io/fattredd/tabby:latest
    ports:
      - "5000:5000"
    volumes:
      - ./config:/app/config
```

Building the docker image
===

You can build the docker image with the following command:

```bash
docker build -t tabby .
```

then you can run it with 
 
```bash
docker run \
  -p 5000:5000 \
  -v $(pwd)/config:/app/config \
  tabby
```
