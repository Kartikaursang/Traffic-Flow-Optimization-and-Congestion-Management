# Adaptive Traffic Signal Timer

This Intelligent Traffic Signal Timer leverages real-time camera feeds from intersections to assess traffic density using YOLO object detection. Based on the analysis, it dynamically adjusts the signal timings to alleviate traffic congestion, enhance commuting speed, and minimize fuel consumption for more efficient traffic flow.

---

## Problem Statement

**Traffic Flow Optimization and Congestion Management**

With increasing urbanization and vehicle density, traffic congestion has become a critical issue in modern cities. Traditional traffic light systems rely on fixed timers, which lack the flexibility to adapt to real-time traffic conditions, leading to inefficiencies and frustration for motorists.

According to the TomTom Traffic Index, cities like **Mumbai**, **Bengaluru**, and **New Delhi** are ranked among the top 10 globally affected by traffic congestion. Commuters in these cities spend significant time stuck in traffic, which adversely impacts their productivity and quality of life while contributing to increased fuel consumption and environmental pollution.

To address these challenges, the **Adaptive Traffic Signal Timer** provides a Computer Vision-based traffic light control system that dynamically adjusts signal durations based on real-time traffic density. This ensures smoother traffic flow, reduced fuel consumption, and enhanced commuter satisfaction.

---

## Features

### **Real-Time Traffic Density Assessment**
- Utilizes **YOLO object detection** to identify and count vehicles from live camera feeds.
- Categorizes vehicles into various classes such as:
  - Cars
  - Motorcycles
  - Buses
  - Trucks
  - Auto-rickshaws

### **Dynamic Signal Timing**
- Adjusts red, green, and yellow light durations dynamically based on vehicle counts.
- Considers additional factors like the number of lanes, average vehicle speed, and traffic density.

### **Traffic Simulation Module**
- Simulates traffic flow at intersections using the **Pygame library**.
- Provides a visual representation of vehicle movements, signal changes, and traffic scenarios.

---

## Motivation

Urban traffic congestion not only delays commuters but also has significant economic and environmental consequences. Key motivations for this project include:

- **Reducing Traffic Congestion**: By prioritizing directions with higher traffic density, the system ensures smoother traffic flow.
- **Improving Commuter Experience**: Dynamically optimized signals reduce waiting times at intersections.
- **Minimizing Fuel Consumption**: Shorter idle times lead to reduced fuel wastage and lower greenhouse gas emissions.
- **Enhancing Urban Mobility**: Efficient traffic management can improve the overall quality of urban living.

---

## Implementation

### **1. Vehicle Recognition Module**
- Identifies and counts vehicles from images captured by traffic cameras.
- Categorizes vehicles into specific classes:
  - Cars
  - Motorcycles
  - Buses
  - Trucks
  - Auto-rickshaws
- Uses **YOLO (You Only Look Once)**, a state-of-the-art object detection model known for its speed and accuracy.

### **2. Traffic Light Control Algorithm**
- Dynamically adjusts traffic light durations based on:
  - Real-time vehicle counts from the Vehicle Recognition Module.
  - Number of lanes at the intersection.
  - Average speeds of different vehicle classes.
  - Specific traffic conditions like peak hours.
- Allocates longer green light durations to high-density directions to ensure smoother and more efficient traffic flow.

### **3. Traffic Simulation Module**
- Developed using the **Pygame library**, this module provides a visual simulation of:
  - Traffic signals dynamically switching based on real-time conditions.
  - Vehicle movements through intersections.
  - Traffic flow under different congestion scenarios.
- Offers an interactive platform to visualize and analyze the system's effectiveness.

---

## Demonstration

### **Vehicle Detection**
The system identifies and classifies vehicles in real time.

<p align="center">
  <img src="./vehicle-detection.jpg" alt="Vehicle Detection" height="400px">
</p>

---

### **Signal Switching Algorithm and Simulation**
Dynamic signal changes and traffic flow simulation.

<p align="center">
  <img src="./Demo.gif" alt="Signal Switching Simulation">
</p>

---

## Benefits

- **Social**: Enhances commuter satisfaction and reduces stress caused by traffic delays.
- **Economic**: Decreases fuel consumption and associated costs.
- **Environmental**: Lowers greenhouse gas emissions by minimizing idle time.
- **Efficiency**: Improves overall traffic management and reduces travel times.

---

## How It Works

1. **Input**: Real-time camera feeds from intersection points.
2. **Processing**: YOLO object detection identifies and counts vehicles.
3. **Decision-Making**: The algorithm determines optimal signal timings based on traffic density.
4. **Output**: Adjusted signal durations dynamically control traffic flow.

---

## Technologies Used

- **YOLO Object Detection**: For real-time vehicle detection and classification.
- **Python**: Core programming language for implementation.
- **Pygame**: For traffic flow simulation.
- **OpenCV**: For processing camera feed and image analysis.

---

## Future Enhancements

- **Integration of GPS and IoT** for city-wide traffic management.
- **Incorporation of weather conditions** to adjust signal timings during adverse conditions.
- **Machine learning** for predictive traffic flow analysis.
- **Mobile app development** for real-time traffic updates.

---

## Conclusion

The **Adaptive Traffic Signal Timer** is a practical and efficient solution to urban traffic congestion. By leveraging computer vision and dynamic algorithms, it improves the quality of life for commuters, reduces environmental impact, and optimizes city traffic systems for future growth.



------------------------------------------
### Demo

* `Vehicle Detection`

<p align="center">
 <img height=400px src="./vehicle-detection.jpg" alt="Vehicle Detection">
</p>

<br> 

* `Signal Switching Algorithm and Simulation`

<p align="center">
    <img src="./Demo.gif">
</p>

------------------------------------------


