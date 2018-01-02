#!usr/bin/env python
# -*- coding:utf-8 -*-
# 导入webdriver，可以调用浏览器
from selenium import webdriver
# 调用PhantonJS浏览器，返回浏览器对象
driver = webdriver.PhantomJS()
# 发送指定页面的get请求
driver.get("https://www.guokr.com/")
# 获取当前页面的网页源码（Unicode字符串）
html = driver.page_source.encode("utf-8")

# 点击指定name属性的a标签
# driver.find_element_by_link_text("立即注册").click()
# 获取当前标签页的截图
# driver.save_screenshot("guokr.jpg")

# driver.find_element_by_id("searchTxt").send_keys(u"圣诞节")

# driver.find_element_by_xpath("//input[@class='gnicon-search']").click()
# driver.save_screenshot("guokr2.png")

# 获取所有标签页的窗口句柄，返回所有标签页的列表
driver_list = driver.window_handles
# print driver_list
# 切换到指定的标签页
driver.switch_to_window(driver.window_handles)
# # 获取当前标签页的截图
driver.save_screenshot("driver_list.png")


# 关闭标签页
# driver.close()

# 关闭浏览器
driver.quit()