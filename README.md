# Online-Market-Place
_A Project Based On Python_

### Languages 

| Python3 |
|----------|
|  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python"  alt="Python" width="55" height="55"/> |  <img src="https://github.com/devicons/devicon/blob/master/icons/c/c-original.svg" title="C"  alt="C" width="55" height="55"/> | 

### Tools Used :
|VsCode| Syder |
|-------|-------|
|<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original.svg" title="VsCode" alt="Vscode" width="55" height="55"/>|<img src="https://github.com/devicons/devicon/blob/master/icons/spyder/spyder-original.svg" title="Spyder" alt="Spyder" width="55" height="55"/>|<img src="https://github.com/devicons/devicon/blob/master/icons/spyder/spyder-original.svg" title="Spyder" alt="Spyder" width="55" height="55"/>|

**1. Introduction:**

The Online Shopping System is a Python-based application that simulates an online shopping platform where users can browse products, place orders, and track their orders. The system is designed to serve both customers and administrators, providing a seamless shopping experience and efficient management of product inventory and orders.

**2. Features:**

- **Customer Features:**
  - Browse Products: Customers can view a list of available products categorized by type, such as smartphones, watches, and AirPods.
    
  - Place Orders: Customers can select products, specify quantities, and place orders.
    
  - Track Orders: Customers can track the status of their orders using order IDs.
  
- **Administrator Features:**
  
  - Login Authentication: Administrators can securely log in to access administrative functionalities.
  - Stock Management: Administrators can update product inventory, including adding new products and adjusting quantities.
  - Order Status Update: Administrators can update the status of orders, such as marking them as shipped or out for delivery.
  
**3. Implementation:**

- **Data Handling:**
  - CSV files are used to store product data, including product details and prices.
    
  - Separate CSV files are maintained for product data and pricing information to facilitate easy updates and modifications.
  
- **User Interface:**
  
  - The user interface is text-based and interactive, allowing users to navigate through product listings and perform actions such as placing orders and updating inventory.
    
  - User inputs are validated to ensure data integrity and prevent errors.

- **Security:**
  
  - User authentication is implemented for administrators to ensure secure access to administrative functionalities.
    
  - Sensitive information such as admin credentials is stored securely and not hard-coded in the source code.

**4. Technologies Used:**

- **Python:** The core programming language used for implementing the application logic.
  
- **CSV Module:** Utilized for reading and writing data to CSV files, facilitating data storage and retrieval.
  
- **Random Module:** Employed for generating unique order IDs for each transaction.
  
- **Tabulate Module:** Utilized for formatting and displaying tabular data in a structured manner.

**5. Future Enhancements:**
- **Database Integration:** Migrate from CSV files to a database management system for improved scalability and performance.
  
- **Graphical User Interface (GUI):** Develop a GUI-based interface to enhance user experience and visual appeal.
  
- **Payment Integration:** Integrate payment processing functionality to enable secure online transactions.
  
- **Order Management System:** Implement a comprehensive order management system to handle order processing, tracking, and fulfillment.
**6.Source Code Details**
Here's a brief point-wise description of the code.
# Source Code Details 
1. **Imports:**
   - The code imports necessary modules: `csv` for CSV file handling, `randint` from `random` module to generate random order IDs, and `tabulate` for tabular data formatting.

2. **Data Initialization:**
   - Admin credentials and product data are initialized from CSV files.

3. **Functions:**

`read_data_from_csv(filename)`: Reads data from a CSV file and initializes a dictionary.

`Id_Generator()`: Generates a random order ID.
   - `display_product_list(product, prices)`: Displays a list of products with their prices.
     
`user_input_saver(...)`: Saves user input data to a CSV file.

`check_availability_and_order(...)`: Checks product availability, takes user input for ordering, and updates the order details.

`shopping_process()`: Initiates the shopping process for customers.

`login_process()`: Handles the login process for admins.

`write_data_to_csv(filename, data)`: Writes data to a CSV file.

`stock_updation(product_list, filename)`: Updates product stock.

`stock_upadation_Menu()`: Displays a menu for stock updation.

`update_order_status(order_id, new_status)`: Updates order status.

`track_order(order_id)`: Tracks an order based on the order ID.

`status_updation_menu()`: Displays a menu for order status updation.

4. **Main Interface:**
   - Prompts the user to choose between customer and admin access.
   - If customer access is chosen, it allows the user to browse products or track orders.
   - If admin access is chosen, it requires authentication and allows the admin to update product stock or order status.

5. **File Structure:**
   - Describes the structure of files used in the project.

6. **Usage Instructions:**
   To run your code, follow these instructions:

1. **Ensure Python is Installed:**

Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/) if you haven't already.

2. **Install Required Dependencies:**
   
   - Open a terminal or command prompt.
   - Navigate to the directory where your code is located.
   - Run the following command to install the required dependencies:
     ```bash
     pip install tabulate
     ```

4. **Run the Main Python Script:**
   - In the same terminal or command prompt, navigate to the directory containing your Python script (`sourcecode.py`).
   - Run the script using the following command:
     ```bash
     sourcecode.py
     ```

5. **Choose User Type:**
   - You'll be prompted to choose between customer and admin access.
   - Enter `1` for admin access or `2` for customer access.

6. **Follow On-Screen Instructions:**
   - Depending on your choice:
     - If you choose customer access, you can browse products, place orders, and track them.
     - If you choose admin access, you can update product stocks or order statuses.

7. **Provide Inputs:**
   - Follow the on-screen instructions to input relevant information, such as product choices, quantities, and login credentials.

8. **Exit the Program:**
   - To exit the program, follow the provided exit options.

9. **Review Output:**
   - After performing actions like placing orders or updating stocks/statuses, review the outputs on the console or in the generated CSV files.

10. **Note:**
   - Make sure to keep the CSV files (`iPhoneData.csv`, `AirpodesData.csv`, `WatchData.csv`, `iPhonePriceData.csv`, `AirpodesPriceData.csv`, `WatchPriceData.csv`, `DataBase.csv`) in the same directory as your Python script.

By following these steps, you should be able to run your code and interact with the SAT Mobile Shopee application.

# Contributors 
   - [Atharva Kote](https://github.com/Atharvkote)
   - [Sairaj Naikwade](https://github.com/sairajnaikwade)
   - [Tushar Nagare](https://github.com/Tusshar123)

# Conclusion 

The Online Shopping System is a versatile and scalable solution for managing online retail operations. By leveraging Python and various modules, the system provides a robust platform for users to browse products, place orders, and track their purchases. With further enhancements and refinements, the system has the potential to become a comprehensive e-commerce solution catering to a wide range of businesses and customers.

## 🔗 Links
[![Telegram Badge](https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AtharvKote)
[![Linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atharva-kote)
[![Twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ImAtharva81)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
)](mailto:atharvkote3@gmail.com)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](discordapp.com/user/1238159826748702824)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/___atharv_81?igsh=MWxseGoyYmlianp6ZQ==)

<p align="center">
     <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>
</p>
