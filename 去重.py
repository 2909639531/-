import os

# 去除文件夹里面的重复文件，如：1.png,1(1),2.png,2(1).png,这样每个东西都有一个自己的副本的情况

now_path = os.getcwd()
print(f"当前路径：{now_path}")

document_path = input("输入文件路径：")
os.chdir(document_path)

document_list = os.listdir()
print(rf"输入文件路径里面的文件列表：{document_list}")

success_count = 0
fail_count = 0
for document in document_list:
    if "(1)" in document:
        original_document = document.replace("(1)", "")
        if os.path.exists(original_document):
            os.remove(document)
            print(f"✅ 已删除副本: {document} (原件 {original_document} 存在)")
            success_count += 1
        else:
            print(f"❌ 没删除副本: {document} (原件 {original_document} 不存在)")
            fail_count += 1

print(f"处理完成，共删除了 {success_count} 个重复文件，{fail_count}个文件删除失败。")
