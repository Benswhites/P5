import swarmClass
import taskClass
import threading
import ArrayLists

swarmClass.CreateProductBot(3)

swarmClass.CreateProcessBot(3)

swarmClass.MakeBotLaunch()

taskClass.AmountBricks()

for i in range(len(ArrayLists.arrayOfProd)):
    threading.Thread(target=taskClass.ProdBotEat).start()

