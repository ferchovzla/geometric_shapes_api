from app_core import create_app

# To do: This place will change later
config = {
    "dev": "config.Development",
    "prod": "config.Production"
}

if __name__ == "__main__":
    #app = create_app(config)
    app.config.from_object(config["dev"])
    app.run()