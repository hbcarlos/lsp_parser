from jupyter_lsp import lsp_message_listener

def _jupyter_server_extension_points():
    return [{
        "module": "lsp_parser"
    }]


def _load_jupyter_server_extension(server_app):
    """
    Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    server_app.log.info("Registered lsp-parser extension.")

    @lsp_message_listener("client")
    async def client_listener(scope, message, language_server, manager):
        print("*"*30, "    CLIENT    ", "*"*30)
        print("Scope:", scope)
        print("Message:", message)
        print("LS:", language_server)
        print("Manager:", manager)
        print("*"*100)
    
    @lsp_message_listener("server")
    async def server_listener(scope, message, language_server, manager):
        print("*"*30, "    SERVER    ", "*"*30)
        print("Scope:", scope)
        print("Message:", message)
        print("LS:", language_server)
        print("Manager:", manager)
        print("*"*100)

# For backward compatibility with notebook server - useful for Binder/JupyterHub
load_jupyter_server_extension = _load_jupyter_server_extension

