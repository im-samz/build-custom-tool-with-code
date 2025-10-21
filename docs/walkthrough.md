# Build a custom tool with code

> Create, test and deploy a tool for your AI Foundry agent to consume.

## A project has been created for you

Check out and test the sample tool. You can open and edit your project files from teh Explorer view on the left, or proceed with onboarding tasks below.

### Open Tool Code

1. From the Explorer view, open the `/src` folder and select `function_app.py`
1. Familiarize yourself with the programming model to build a custom tool that is called through the model-context protocol (MCP).

## Run/test sample tool

Press Run to start your local host, and test your tool in the Agent Playground by asking, "what's 9 + 10?".

### Run/test tool

1. From the `/src` folder, run `func start` to run the MCP server on the localhost.
1. From `/.vscode/mcp.json`, ensure that `local-tool-server` is started.
1. Open chat and select Agent mode with any model.
1. Test the sample tools with any of the following prompts:
    1. "Hello, my name is {YOUR_NAME}"
    1. "What's 9 + 10?"
    1. "What's the weather in Seattle today?"

## Build your custom tool

Modify the sample tool with your custom code. To test your iteration, press Run to restart the local host with your latest changes.

### Modify the sample tool

The scaffolded project is designed to be hosted on Azure Functions. It uses the `MCP Tool Trigger` to abstract the complexity of building a full-fledged remote MCP server. If you're new to building serverless applications on Azure Functions, you can refer to [APPENDIX: Best practices for building serverless MCP tools].

### Run/test tool

1. After you've modified the sample tool into your desired custom tool, repeat the same steps to iteratively test it.
1. From the `/src` folder, run `func start` to restart the MCP server running on local host with your latest changes.
1. From `/.vscode/mcp.json`, ensure that `local-tool-server` is started.
1. Open chat and select Agent mode with any model.
1. Test your custom tool with the appropriate prompts.

## Deploy tool

Once you're done writing and testing your tool, you can deploy it to Azure using Azure Developer CLI (`azd`). This will provision an Azure Function app and your project will be deployed to it. Your Foundry agent will be configured to authenticate with the tool.

### Deploy to Azure

1. From the root directory, run `azd up`.

## Save project code

After a successful deployment, your Foundry agent can now call your custom tool. You may exit now, but you can download a copy of the code or push it to a GitHub repository to edit your tool later.

### Save

1. To save locally, open the command palette (CTRL/CMD+SHIFT+P) and search for `Workspaces: Save Workspace As...`
1. To push to GitHub, open the command palette (CTRL/CMD+SHIFT+P) and search for `Publish to GitHub`

Congratulations on building your custom tool with code. You may exit the VS Code for the Web environment and test your custom tool from the Foundry Agent Builder.
