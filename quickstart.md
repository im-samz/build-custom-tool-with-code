# Remote MCP Server with Azure Functions (Python)

A Model Context Protocol (MCP) server running on Azure Functions that provides custom tools and capabilities.

> [!TIP]
> You can refer to [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) for detailed getting started instructions.

## Quick Start

### 1. Deploy to Azure

```bash
azd up
```

This command will provision Azure resources and deploy your function app.

### 2. Get MCP Configuration Values

After deployment, retrieve the required configuration:

**Remote MCP endpoint:**

Your MCP remote URL will be: `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`.

You can obtain `FUNCTION_APP_NAME` by running the following command:

```bash
azd env get-values | grep AZURE_FUNCTION_APP_NAME

```

**System Key for Authentication:**

You can obtain the `mcp_extension` system key by running the following command:

```bash
az functionapp keys list --name <FUNCTION_APP_NAME> --resource-group <RESOURCE_GROUP> --query systemKeys.mcp_extension --output tsv
```

### 3. Configure MCP Client

Starting the `remote-hello-world` MCP server in `./.vscode/mcp.json` will prompt you to provide:

- App name (your Azure Function app name)
- `mcp_extension` key

No need to construct the remote URL manually.

## Development

**Local Development:**

```bash
cd src
func start
```

**Redeploy after changes:**

```bash
azd deploy
```
