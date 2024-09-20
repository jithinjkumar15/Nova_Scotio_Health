# Databricks notebook source
client_id = dbutils.secrets.get(scope = "covid19-scope",key = 'covid19-client-id')
tenant_id = dbutils.secrets.get(scope = "covid19-scope",key = 'covid19-tenant-id')
secret_id = dbutils.secrets.get(scope = "covid19-scope",key = 'covid19-secret-id')

# COMMAND ----------

##setting up access to ADLS storage acoount
#service_credential = dbutils.secrets.get(scope="<secret-scope>",key="<service-credential-key>")

spark.conf.set("fs.azure.account.auth.type.covidlearnstorage.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.covidlearnstorage.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.covidlearnstorage.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.covidlearnstorage.dfs.core.windows.net", secret_id)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.covidlearnstorage.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://raw@covidlearnstorage.dfs.core.windows.net"))

# COMMAND ----------


