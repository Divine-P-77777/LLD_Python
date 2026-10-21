Without Observer Pattern
The weather station would need to know about every single device and manually update each one when the temperature changes.


This creates a big problem:
1. Weather station is tightly connected to all devices
2. Adding a new device means changing weather station code
3. Removing a device means changing weather station code again
4. Weather station depends on specific device types


Observer Pattern Benefits
Loose Coupling: The main object (like WeatherStation) doesn't need to know anything about the specific devices. It just sends notifications to whoever is listening, without caring what type of device it is.
Easy to Scale: You can add as many new devices as you want (phones, TVs, smartwatches, etc.) without changing a single line of code in the WeatherStation. Just register the new device and it starts receiving updates automatically.
Flexible at Runtime: Devices can join or leave the notification list anytime while the program is running. A device can start listening when it needs updates and stop listening when it doesn't.


Observer Pattern Use Cases
Event Listeners in Apps: When you build apps with buttons and forms, the Observer Pattern helps handie user actions. For example, when someone clicks a button or types in a text box, all the listeners get notified automatically and can react accordingly.
Stock Price Tracking: Imagine you're tracking Reliance or TCS stock prices. When the price changes, all investors and trading systems that are watching that stock get instant notifications about the new price. They don't need to keep checking manually.
News Apps and Blogs: When a news website publishes a new article, all users who have subscribed to that website automatically receive notifications. Like how you get alerts when your favorite blog posts something new.
Social Media Updates: Think of Instagram or Twitter. When someone you follow posts a new photo or tweet, you get a notification.
You're an observer, and the account you follow is the subject. When they post (subject changes), all followers (observers) are notified.



# Observer Design Pattern

## Definition
Defines a one-to-many relationship where a subject
notifies all registered observers when its state changes.

## Components

1. Subject → WeatherStation
   Maintains observers and notifies them of changes.

2. Observer → Observer
   Defines the update() contract.

3. Concrete Observers → PhoneDisplay, TV
   Implement update() to react to changes.

## Bad Design
WeatherStation directly creates PhoneDisplay.

Problem: Tight coupling; adding new displays requires
modifying the weather station.

## Good Design
WeatherStation depends on the Observer abstraction.
Displays register and unregister independently.

## Benefits
- Loose coupling
- Easy extensibility
- Dynamic subscriptions
- Multiple observers receive updates

## Key Flow
Temperature changes
    ↓
WeatherStation
    ↓
notify_observers()
    ↓
PhoneDisplay.update()
TV.update()

## Real-world Examples
- YouTube channel subscriptions
- Notification systems
- Stock price alerts
- GUI event listeners
- Weather applications