# Third party modules
import uvicorn


# ---------------------------------------------------------
#
def main():
    """ Start uvicorn program. """
    uv_config = {'app': 'src.web.main:app', 'port': 1029}
    """ uvicorn startup parameters. """

    uvicorn.run(**uv_config)


if __name__ == "__main__":
    main()