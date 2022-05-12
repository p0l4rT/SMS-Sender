
<p align="center">
<img src="https://camo.githubusercontent.com/460d9e93600497c82515ce338f834a230f570fde783e2cd609b747f2f68c2b5f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d312e302d6f72616e6765">
  
<img src="https://camo.githubusercontent.com/2bb630e2707a04100cd270fd944d22816241c37b68a5a1629257920c65e17891/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c7565">

<img src="https://camo.githubusercontent.com/1bab4c20414ff279288207bdf3a4e891389390ed8f7ffe330617182214046795/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e67756167652d507974686f6e332d79656c6c6f77">

</p>

<p align="center"><img src="https://user-images.githubusercontent.com/104868654/167976018-0f0b60a7-3943-4035-a91a-105c7bb89154.png"></p>

<h1 align="center">Send anonymous SMS via Terminal</h1>
<p align="center">This tool was tested over Linux and Windows, but it was created to work with every Operative System.</p>
<br>
<h2>Support</h2>
<h3">This project was made with ♥ for you, but if you want to support this project<br>you can donate some coins in my Patreon profile.</h3>
<br><br>
<p><a href="https://www.patreon.com/polartech_wh"><img src="https://user-images.githubusercontent.com/104868654/167985820-7f25298b-07d9-4308-a133-13e9f21424ef.png"></a></p>

<details>
<summary><h2>Read before download</h2></summary>
  
I decided to make this script with the paid service because the free SMS is only available in some countries not specified by the provider.
So I decided to do it like this to offer a better experience.

I recommend buying one of the textbelt.com pLANS, there are very affordable and you can send SMS without waiting 24 hours and at any time.

<h3>You have two purchase options:</h3>
  
1. Sign up to buy credits and an api
2. Buy credits and an api without registration. (Recommended)
  
There are packages starting at $3 for 50 SMS that you can use in the US/Canada
or 5 dollars for 30 SMS Worldwide.
  
  <table>
    <tr>
      <th>
<h3>REGIONS AND BASIC PLAN PRICES</h3>
      </th>
    </tr>
    <tr>
      <td>
<table>
   <thead>
      <tr>
         <th>REGION</th>
         <th>QUOTA</th>
         <th>PRICE</th>
      </tr>
   </thead>
   <tbody>
      <tr class="US/CA">
         <td>US/Canada</td>
         <td>50 Texts</td>
         <td>$3 USD</td>
      </tr>
      <tr class="EU">
         <td>Europe</td>
         <td>30 Texts</td>
         <td>$5 USD</td>
      </tr>
      <tr class="ASI/OCE">
         <td>Asia/Oceania</td>
         <td>30 Texts</td>
         <td>$5 USD</td>
      </tr>
       <tr class="ME/AFR">
         <td>MiddleEast/Africa</td>
         <td>25 Texts</td>
         <td>$5 USD</td>
      </tr>
      <tr class="AME">
         <td>Americas</td>
         <td>30 Texts</td>
         <td>$5 USD</td>
      </tr>
         <tr class="WW">
         <td>Worldwide</td>
         <td>30 Texts</td>
         <td>$5 USD</td>
      </tr>
   </tbody>
</table>
              </td>
    </tr>
  </table>
  
  Do you wanna buy any plan?<br>
  https://textbelt.com/purchase/
  
</details>

<details>
<summary><h2>Installation</h2></summary>
  <ul>
    <il>
      <h3>1. Install python3</h3>
      <b>UBUNTU/DEBIAN</b><br>
      <code>sudo apt-get install python3</code><br><br>
      <b>FEDORA</b><br>
      <code>sudo dnf install python3</code><br><br>
      <b>ARCH LINUX (Any Arch based distro. E.g.: Manjaro)</b><br>
      <code>sudo pacman -S python3</code>
    </il>
    <il>
     <h3>2. Clone this git</h3>
      <code>cd [PATH DIR]</code><br>
      <code>git clone https://github.com/p0l4rT/SMS-Sender.git</code><br>
      <code>cd SMS-Sender</code>
    </il>
    <il>
     <h3>3. Install required modules</h3>
      <code>pip install -r requierements.txt</code> or <code>pip3 install -r requierements.txt</code><br>
    </il>
    <il>
     <h3>4. Set permissions</h3>
      <code>sudo chmod +x *</code><br>
    </il>
    <il>
     <h3>5. Reboot your pc</h3>
    </il>
  </ul>
</details>

<details>
<summary><h2>Preparing</h2></summary>
  <ul>
    <il>
    <h3>1. Set your API KEY in credentials.ini</h3><br>
      <p>If you are on windows you can edit the file with notepad. Save it and ready</p>
      <img src="https://user-images.githubusercontent.com/104868654/168010107-9f96696e-817d-4c95-bd53-466b517f5297.png">
      <br><br>
      <p>If you are on linux you can edit it with any text editor, IDE or using:</p>
      <code>sudo nano credentials.ini</code><br><br>
      <img src="https://user-images.githubusercontent.com/104868654/168011572-6cfd37a7-5bfb-483f-95cc-ebfe9841501b.PNG">
    </il>
  </ul>
</details>

<details>
<summary><h2>How to use</h2></summary>
  <ul>
    <il>
      <h3>1. Set the SMS-Sender path</h3>
      <code>cd [SMS-Sender PATH]</code>
    </il>
    <il>
      <h3>2. Run the script</h3>
      <code>python3 sendsms.py</code> or <code>python sendsms.py</code>
    </il>
  </ul>
</details>
