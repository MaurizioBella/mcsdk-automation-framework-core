# Salesforce Marketing Cloud - SDK Automation with SwaggerCodegen

## Overview

This repo is part of the Salesforce Marketing Cloud SDK Automation Framework. It holds the Open Api Specification json file which is used for the SDK Generation in four different languages ([C#](https://github.com/salesforce-marketingcloud/mcsdk-automation-csharp), [Java](https://github.com/salesforce-marketingcloud/mcsdk-automation-java), [Php](https://github.com/salesforce-marketingcloud/mcsdk-automation-php) and [Node](https://github.com/salesforce-marketingcloud/mcsdk-automation-node)).

## Contents

- [Swagger Code Gen](https://github.com/swagger-api/swagger-codegen) CLI
- [Open API Specification for Salesforce Marketing Cloud REST Routes](https://github.com/salesforce-marketingcloud/mcsdk-automation-framework-core/blob/master/resources/sfmc-openapi-v2.json)
- Python Scripts for SDK Automation

## Supported operations

file `sfmc-openapi-v2.json`

- (POST /sms/v1/queueMO)[https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/postQueueMO.html]
- (/interaction/v1/events)[https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/postEvent.html]
- asset
- campaign
- transactionalMessaging

## Getting Started

To add a new REST route to the generated SDK,

1. Create your own branch and modify the [Open API Spec file](https://github.com/salesforce-marketingcloud/mcsdk-automation-framework-core/blob/master/resources/sfmc-openapi-v2.json)
2. Make sure the format is correct without any errors. [Swagger Online Editor](https://editor.swagger.io/) is an amazing tool to play with the Open Api Spec files. It has the ability to identify formatting errors.
3. Push the changes to remote and create a PR against the most recent version branch from your new branch.
4. This PR would trigger the Travis CI process.
5. At the end of the CI Process, a new branch would be created on the [SDK Repo](https://github.com/salesforce-marketingcloud/mcsdk-automation-csharp). Also a PR would be created against the most recent version branch in the SDK Repo.
6. You can then download the SDK project and test the changes in the new branch.
7. As of now, the process of merging the code to the Master branch is set to Manual for first phase. It would also be automated in future releases.

### Note

Any changes to the existing Open API Spec file like changing the name of the parameters, making an optional parameter required, changing the request/response model names introduce breaking changes and will break the customers who are using the Automations SDKs.

## Contact us

- Request a [new feature](https://github.com/salesforce-marketingcloud/mcsdk-automation-framework-core/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc), add a question or report a bug on GitHub.
- Vote for [Popular Feature Requests](https://github.com/salesforce-marketingcloud/mcsdk-automation-framework-core/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) by making relevant comments and add your reaction. Use a reaction in place of a "+1" comment:
  - 👍 - upvote
  - 👎 - downvote

## License

By contributing your code, you agree to license your contribution under the terms of the [BSD 3-Clause License](https://github.com/salesforce-marketingcloud/mcsdk-automation-framework-core/blob/master/LICENSE.md).
