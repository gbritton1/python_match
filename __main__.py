from order import Order
from customer import Customer
from order_item import OrderItem
from tramp import tramp

def main():
    HoG = Customer('Heart of Gold', 'The Milky Way Galaxy', False)
    Millis = Customer('Milliways Restaurant', 'Magrathea', True)
    Arthur = Customer('Arthur Dent', 'Earth', False)
    drive = OrderItem('Infinite Improbability Drive', 'IID1', 1, 100, True)
    Trillian = OrderItem('Date with Trillian', 'DWT', 42, 1000000, True)
    choc = OrderItem('Chocolate', 'CHOC', 200, 250, False)

    ord1 = Order(1, 'Terra', False, False, HoG, [drive])
    ord2 = Order(2, 'Heart of Gold', True, False, Arthur, [Trillian, choc])
    ord3 = Order(3, 'Magrathea', True, False, Millis, [choc])

    Order.orders = [ord1, ord2, ord3]
    Order.notify_backordered(Order.orders, "backordered items")
    Order.orders = Order.mark_backordered(Order.orders, 3, 'CHOC')
    # print(len(
    #     Order.count_expedited_orders_with_backordered_items(Order.orders))
    #     )
    # print(Order.count_expedited_orders_with_backordered_items_rec(Order.orders))
    # print(Order.count_expedited_orders_with_backordered_items_tail(Order.orders))
    print(tramp(Order.count_expedited_orders_with_backordered_items_tramp, Order.orders))
    print(Order.count_expedited_orders_with_backordered_items_comp(Order.orders))
    # print(Order.count_expedited_orders_with_backordered_items_higher(Order.orders))
main()
