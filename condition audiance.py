audiance_group="kid","teen","adult"
audiance="new born"
if audiance in audiance_group:
  if audiance=="kid":
    print("free")
  elif audiance=="teen":
    print("half price")
  else:
    print("full price")
else:
    print("bether stay at home")