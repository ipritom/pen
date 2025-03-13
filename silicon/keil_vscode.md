# How to Setup Keil inside VSCode

Keil MDK (Microcontroller Development Kit) is a powerful development environment for ARM Cortex-M microcontrollers. While Keil uVision IDE is commonly used, developers often prefer Visual Studio Code (VS Code) for its flexibility and powerful extensions.

In this brief staightforward article, I'll show how you can get functionalities of Keil inside vscode. 

This article presumes following points.
* You have already installed [VScode](https://code.visualstudio.com/)

* You have already installed C/C++ Extenstion Pack in VScode.

* You are using stlink-v2 for uploading program to your board. 

* You have already installed [stlink-v2 driver software](https://www.st.com/en/development-tools/stsw-link009.html).

* You have some primary knowledge of using **Keil uVision IDE**.

Now follow the following steps to use Keil inside VScode. 

# Step 1 : Installing Necessary Extension

Go to the `Extensions` tab in VS Code and search for the keyword "arm". You'll see the necessary extensions developed by Arm, along with a verified badge.

Simply install the extensions shown in the following picture:

![](https://res.cloudinary.com/djqcqqueb/image/upload/v1741881303/vscode_keil/f1i1ambjyvold8mzvfwe.png)

One thing to remember: the latest versions of VSCode are highly intelligent. Many installations and adjustments are handled automatically. You just need to initiate the process.

 
# Step 2: Creating a new Project

After the successfull installation you'll see two new buttons in the sidebar - `CMSIS` and `Device Manager`.

From `CMSIS` you can create a new project.

![](https://res.cloudinary.com/djqcqqueb/image/upload/v1741881303/vscode_keil/xnkb3qg2bzqwe0ddsrpk.png)

After creating the new project, select the device. In this example, we are choosing an STM32 MCU. I've a [Blue Pill board](https://stm32-base.org/boards/STM32F103C8T6-Blue-Pill.html), which have STM32F103C8T6. 

![](https://res.cloudinary.com/djqcqqueb/image/upload/v1741881302/vscode_keil/cjleir4qwdubm8vygtz2.png)

# Step-3: Know Your Programming Interface

After you successfully create a project from the `CMSIS` tab you'll able to see the marked tools. 

![](https://res.cloudinary.com/djqcqqueb/image/upload/v1741881302/vscode_keil/g5pinvt4ydjwtmrvxio8.png)

The first button is `Build Soluton` which will build your written code. 

The next is `Run` buttion. If your board is connected through ST-Link and ST-Link is connected to VScode succesfully, you'll able to flash your program to your board.



# Step 4: Select ST-Link

Connect your STM32 PCB with ST-Link. And go to the `Device Manager`. You'll see ST-Link is connected. 

![](https://res.cloudinary.com/djqcqqueb/image/upload/v1741881302/vscode_keil/moqa4v23wkj8gocxxnrr.png)

# Step 5: Upload Your Code

If all the installations are correct and your board is connected to your PC through ST-Link, you will be able to flash the program to your board.


![](https://res.cloudinary.com/djqcqqueb/image/upload/v1741882833/vscode_keil/kyup8gq25kkt1pjhgxum.png)


Now you have Keil inside VScode. Happy coding!