from modules import modules

with open("README.md", "r+", encoding='utf-8') as fp:
    before_modules, _, after_modules = fp.read().split("<!--modules-->")
    fp.seek(0)
    fp.write(before_modules)
    fp.write("<!--modules-->\n")
    for module in sorted(modules):
        fp.write(f"- **{module.name}**: {module.summary}\n")
    fp.write("\n<!--modules-->")
    fp.write(after_modules)