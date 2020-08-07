# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by curz0n on 2017年5月19日
# Updated on 2018-6-1


import os
import shutil
import sys
import datetime


def createdNewModule(moduleName):

	projectPath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
	moudlePath = os.path.join(projectPath,"xposedModules",moduleName)
	if os.path.exists(moudlePath):
		print("[-] Module {0} is already exists.".format(moduleName))
		return

	#复制模板
	shutil.copytree(os.path.join(projectPath,"app"),moudlePath,ignore = shutil.ignore_patterns("libs","*.iml","androidTest","test"))

	#更新包名
	os.rename(os.path.join(moudlePath,"src/main/java/com/xposed/hooks/xposedmodules"),
		os.path.join(moudlePath,"src/main/java/com/xposed/hooks",moduleName))

	#更新文件内容
	updateFiles = ["src/main/assets/xposed_init",
	"src/main/AndroidManifest.xml",
	"src/main/res/values/strings.xml",
	"build.gradle",
	"src/main/java/com/xposed/hooks/{0}/XposedHookLoadPackageEntry.java".format(moduleName)]
	for file in updateFiles:
		filePath = os.path.join(moudlePath,file);
		content = open(filePath).read()
		result = content.replace("xposedmodules",moduleName)
		#更新代码创建时间
		if updateFiles.index(file) == 3:
			result =result.replace("2017/5/19",datetime.datetime.now().strftime('%Y/%m/%d'))
		open(filePath,"w").write(result)


	open(os.path.join(projectPath,"settings.gradle"),"w").write("include 'xposedModules:{0}'".format(moduleName))

	print("[+] Xposed module {0} is created.".format(moduleName))


def main():
	if (len(sys.argv) != 2):
		print("Usage: {filename} new_xposed_module_name".format(filename=os.path.basename(__file__)))
		return
	createdNewModule(sys.argv[1])


if __name__ == '__main__':
	main()
