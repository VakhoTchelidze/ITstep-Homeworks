
#ესაა ლისტის კომპონენტის მონაცემი - ცალკეული ნოუდი სადაც უნდა შევინახოთ ინფორმაცია(შესანახი მონაცემი და ლინკი მომდევნო მონაცემთან)
class ListNode:
    def __init__(self, value):
        #აქ ვინხავთ მონაცემს
        self.value = value
        #აქ ვინახავთ მომდევნო ელემენტს
        self.next = None

#ეს არის უშუალოდ მწკრივის კლასი
class LinkedList:
    #შემნისას ვამატებთ საწყის ელემენტს
    def __init__(self, value):
        #ჰედის მონაცემს ვინახავთ ლისტ ნოუდის კლასში სადაც შექმნილი გვაქვს ნოუდის სტრუქტურა
        self.head = ListNode(value)
        #აქ ვინახავთ ლისტის სიგრძეს
        self.length = 1

    #ლისტში ელემენტის ჩამატების ფუნქცია
    def append(self, value):
        #დროებითად საწყის ელემენტს ვინახავთ ქურენთ ნოუდის ცვლადში რადგან შევძლოთ საწყისი ელემენტიდან ბოლო ელემენტამდე მისვლა
        current_node = self.head

        #ბოლო ელემენტია ის რომლის ნექსტ ელემენტიც არის None, ამ ვაილ ლუპით გადავდივართ ელემენტიდან ელემენტზე მანამ სანამ არ მივალთ ბოლო ელემენტტთან
        while current_node.next is not None:
            current_node = current_node.next

        # როცა ბოლო ელემენტზე მივალთ ლისტნოუდის კლასის დამხარებით დავამატებთ ახალ ელემენტს
        new_node = ListNode(value)
        #ქურენთ ნოუდი ვაილ ლუპის მერე იქნება ბოლო ელემენტზე ამიტომ ბოლო ელემენტის ნექსთს რომელიც ნონია ჩავანაცვლებთ ახალი ელემენტით
        current_node.next = new_node
        #აქ ვითვლით ლისტის სიგრძეს
        self.length += 1

    #მონაცემის ჩამატების ფუნქცია - აქ სამი სცენარია - როცა ჩამატება გვინდა თავში, ბოლოში და სხვა ადგილას.
    def insert(self, value, index):
        #აქ ვინთვლით ლისტის ინდექსებს
        last_index = self.length - 1
        # ეს გვჭირდება ინდექსაციისთვის
        i = 0

        #თუ თავში გვინდა ჩამატება
        if index == 0:
            # ძველი მონაცემის ცვლადში ვინახავთ ჰედს
            old_head = self.head
            # შემდეგ ვამატებთ ნოუდს და ვინახავთ ჰედის ცვლადში
            self.head = ListNode(value)
            #ახალი ჰედის ნექსტში ვინახავთ ძველ ჰედს
            self.head.next = old_head
            #ვამატებთ სიგრძის ცვლადს 1-ს
            self.length += 1

        # თუ ვამატებთ სიის ბოლოს
        elif index == last_index+1:
            # უბრალოდ აპენდ ფუნქციით ვამატებთ ახალ მონაცემს
            self.append(value)

        # როცა სიის შუაში ვამატებთ
        elif 0 < index < last_index + 1:
            #ქურენთ ნოუდის ცვლადში ვინახავთ ჰედს რომ შევძლოთ ნექსთ ფუნქციით იმდენჯერ გადასვლა სანამ სასურველ ადგილზე არ მივალთ
            current_node = self.head

            #ვაილ ციკლით ვითვლით გადასვლებს იქამდე დანამ i არ იქნება ჩვენ მიერ მითითებული იდექსის წინ
            while i != index-1:
                current_node = current_node.next
                i += 1
            ვაილ ლუპის ბოლოს ქურენთ ნოუდში გვექნება

            new_node = ListNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

        elif index > last_index + 1 or index < 0:
            print("Index Is Out Of Range")


    def remove(self, index):
        last_index = self.length - 1
        i = 0

        if index == 0:
            self.head = self.head.next
            self.length -= 1

        elif index == last_index:
            current_node = self.head

            while i < last_index - 1:
                current_node = current_node.next
                i += 1

            current_node.next = None
            self.length -= 1

        elif 0 < index < last_index:
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1

            deleted_element = current_node.next
            current_node.next = deleted_element.next
            self.length -= 1

        elif index > last_index + 1 or index < 0:
            print("Index Is Out Of Range")




    def printList(self):
        current_node = self.head
        print(f"{current_node.value} ->", end="")

        while current_node.next is not None:
            current_node = current_node.next
            print(f" {current_node.value} ->", end="")