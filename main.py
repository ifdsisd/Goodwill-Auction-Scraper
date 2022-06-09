import auctionWatch
import threading



items = auctionWatch.loadItems("itemsForAuction.items")
auction =  auctionWatch.auctionMonitor(items[0],30)


print(auction.currentBid().text)
# for i in urls:
#     print(i)
    
#     items.append(auctionWatch.auctionMonitor(i,30))
# for i in items:
#     process = threading.Thread(target = i.timeLeft)
#     process.start()
# process.join()
