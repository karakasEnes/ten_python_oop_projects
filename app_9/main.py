import api
import justpy as jp


jp.Route('/api', api.Api.serve)
jp.justpy(port=8005)
