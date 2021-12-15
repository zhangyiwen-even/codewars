'''
For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.
The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.
The following are some examples of how this class is used:
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count # should == 2
helper.item_count # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid
# page_ndex takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid
对于本练习，您将增强对页面赋的掌握。您将完成PaginationHelper类，这是一个实用程序类，有助于查询与数组相关的分页信息。
该类旨在接收值数组和一个整数，该整数指示每页允许多少个项目。集合/数组中包含的值的类型无关。
以下是有关如何使用此类的一些示例：
helper = PaginationHelper（['a'，'b'，'c'，'d'，'e'，'f']，4）
helper.page_count＃应该== 2
helper.item_count＃应该== 6
helper.page_item_count（0）＃应该== 4
helper.page_item_count（1）＃最后一页-应该== 2
helper.page_item_count（2）＃应该== -1，因为页面无效
＃page_ndex获取项目索引并返回其所属的页面
helper.page_index（5）＃应该== 1（从零开始的索引）
helper.page_index（2）＃应该== 0
helper.page_index（20）＃应该== -1
helper.page_index（-10）＃应该== -1，因为负索引无效
'''

# TODO: complete this class

class PaginationHelper:
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page

  def item_count(self):
      return len(self.collection)

  def page_count(self):
      if len(self.collection) % (self.items_per_page) == 0:
            return len(self.collection) / (self.items_per_page)
      else:
            return len(self.collection) / (self.items_per_page) + 1  

  def page_item_count(self,page_index):
      if page_index >= self.page_count():
            return -1
      elif page_index == self.page_count() - 1:
            return len(self.collection) % (self.items_per_page) or self.items_per_page
      else:
            return (self.items_per_page)

  def page_index(self,item_index):
      if item_index >= len(self.collection) or item_index <= 0:
            return -1
      else:
            return item_index / (self.items_per_page)
p = PaginationHelper(['a','b','c','d','e','f'], 4)
print(p.item_count)