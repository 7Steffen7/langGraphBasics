from unstructured.partition.pdf import partition_pdf

elements = partition_pdf("IASC.pdf")
for element in elements:
    print(f"{element.metadata.page_name} - {element.text}")