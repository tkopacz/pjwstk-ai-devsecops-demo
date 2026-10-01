param releaseSha string
resource marker 'Microsoft.Resources/tags@2021-04-01' = {
  name: 'default'
  properties: {
    tags: union(resourceGroup().tags, { approvedRelease: releaseSha })
  }
}
output approvedRelease string = releaseSha