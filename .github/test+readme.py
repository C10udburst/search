from modules import modules

with open("README.md", "r+", encoding='utf-8') as fp:
    before_modules, modules, after_modules = fp.read().split("<!--modules-->")
    fp.seek(0)
    fp.write(before_modules)
    fp.write("<!--modules-->\n")
    for module in modules:
        fp.write(f"- {module.name}: \n{module.summary}\n\n")
    fp.write("\n<!--modules-->")
    fp.write(after_modules)