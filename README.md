# Absher
# Mammshak - ممشاك

##  Project Overview
The *Vehicle Incident AI Simulator* is a web-based dashboard system designed to simulate car accidents and automatically generate incident reports. It allows users to visualize vehicle data, GPS location, damage assessment, and a 360° accident view — all without the need for physical hardware. This project is ideal for hackathons, demonstrations, or training scenarios.

---

##  Problem Statement
- Manual accident reporting is time-consuming and relies on human intervention, causing delays in emergency response.  
- Assessing vehicle damage on-site is challenging and often subjective.  
- Simulating advanced accident reporting systems is difficult without actual hardware for demonstration purposes.

---

##  Innovative Solution
- *Simulated Vehicle Data*: Automatically generate owner info, license plate, VIN, and car model.  
- *AI-based Damage Simulation*: Simulate damage severity (Low, Medium, High) and affected areas (Front-Left, Front-Right, Rear-Left, Rear-Right).  
- *Automated Report Generation*: Generate a detailed incident report ready for submission to authorities (e.g., Najm or EMS).  
- *Interactive Dashboard*: Real-time visualization of vehicle info, GPS location, damage charts, and a 360° accident video.

All data is *mocked*, enabling full demonstration without any physical sensors or devices.

---

##  How It Works
1. User clicks *“Simulate Crash”* on the dashboard.  
2. System generates:  
   - Vehicle data (owner, plate, model, VIN).  
   - Damage analysis using AI simulation.  
   - GPS location (mock coordinates).  
   - Dashboard updates with charts, map, and 360° video.  
3. A detailed report is automatically generated.  
4. User can click *“Send Report”* to simulate submitting the incident to emergency services.  

---

##  Technologies Used

### Backend
- *Python 3.10+*  
- *Flask* (API endpoints, data simulation, report generation)  
- *Random* (simulate AI damage data)

### Frontend
- *HTML5 & CSS3*  
- *Bootstrap 5* (responsive dashboard layout)  
- *JavaScript (ES6)* (API calls, interactive dashboard)  
- *Chart.js* (damage severity visualization)  
- *Leaflet.js* (GPS map visualization)  

### Additional
- *360° Video* (optional, simulated accident footage)

---

##  Features & Innovations
- Fully *mocked system*, no hardware required.  
- *Interactive and modern dashboard* for a professional presentation.  
- *Automatic incident report generation* for faster decision-making.  
- *Expandable architecture* for future integration with real sensors or advanced AI models.  
- Ideal for **hackathons, demos, and education
