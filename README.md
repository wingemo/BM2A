# Business Model to API (BUSINESSMODEL2API)

## Overview

This project aims to bridge the gap between your BPMN (Business Process Model and Notation) model and API development. In this README, we will outline the key concepts and how verbs in your BPMN model correspond to actions for data storage references, ultimately leading to the creation of API endpoints.

## Verbs and Actions

In your BPMN model, these verbs serve as actions for your data storage references, symbolizing the diverse operations essential to your process. Subsequently, these verbs will be translated into corresponding API endpoints:

- **GET** -> **RETRIEVE**
- **POST** -> **CREATE**
- **PUT** -> **UPDATE**
- **DELETE** -> **DELETE**

For example:

**DATA STORAGE REFERENCE:** {**CREATE** [NAME, ID, TIMESTAMP]}

## How it Works

The BPMN XML file parser analyzes the BPMN model to identify data references and the operations that should be possible. It then generates endpoints for these operations, which are implemented in different APIs based on the type of data they operate on.
