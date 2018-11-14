#include <OneWire.h>
OneWire  ds(10);  // 连接arduino10引脚

// 内置led端口
int innerLed = 13;

//人体红外检测
int peoplePin = 2;
int ispeople = 0;


int knobPin = A4;
int soilPin = A2;
int waterPin = 8;
int lightPin = A0;
int soundPin = A5;

//0-1024 旋钮值
int knobValue = 400;

//0-1024 土壤越干 值越大
int soilValue = 0;

//0-1024 光越强 值越大
int lightValue = 0;

int soundValue = 0;

// 摄氏度表示
float heatValue = 0.0;


byte i;
byte present = 0;
byte type_s;
byte data[12];
byte addr[8];
float celsius, fahrenheit;
 
 
void setup(void) {
  Serial.begin(9600);
  T_init();

  pinMode(knobPin,INPUT);
  pinMode(soilPin,INPUT);
  pinMode(waterPin,OUTPUT);
  pinMode(lightPin,INPUT);
  pinMode(innerLed,OUTPUT);
  pinMode(peoplePin,INPUT);

  
}


int T_init(void)
{
    if ( !ds.search(addr)) {
    return 0.0; 
  }

  if (OneWire::crc8(addr, 7) != addr[7]) {
    
      return 0.0;
  }
  
  // the first ROM byte indicates which chip
  switch (addr[0]) {
    case 0x10:
      //Serial.println("  Chip = DS18S20");  // or old DS1820
      type_s = 1;
      break;
    case 0x28:
      //Serial.println("  Chip = DS18B20");
      type_s = 0;
      break;
    case 0x22:
      //Serial.println("  Chip = DS1822");
      type_s = 0;
      break;
    default:
      //Serial.println("Device is not a DS18x20 family device.");
      return;
  } 
 

  return 0;
}

float getTemplate(void) {
  ds.reset();
  ds.select(addr);
  ds.write(0x44,1);         // start conversion, with parasite power on at the end

  // ..........too long...
  delay(700);     // maybe 750ms is enough, maybe not
  // we might do a ds.depower() here, but the reset will take care of it.
   
  present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE);         // Read Scratchpad


  for ( i = 0; i < 9; i++) {           // we need 9 bytes
    data[i] = ds.read();
  }
 
  // convert the data to actual temperature
 
  unsigned int raw = (data[1] << 8) | data[0];
  if (type_s) {
    raw = raw << 3; // 9 bit resolution default
    if (data[7] == 0x10) {
      // count remain gives full 12 bit resolution
      raw = (raw & 0xFFF0) + 12 - data[6];
    }
  } else {
    byte cfg = (data[4] & 0x60);
    if (cfg == 0x00) raw = raw << 3;  // 9 bit resolution, 93.75 ms
    else if (cfg == 0x20) raw = raw << 2; // 10 bit res, 187.5 ms
    else if (cfg == 0x40) raw = raw << 1; // 11 bit res, 375 ms
    // default is 12 bit resolution, 750 ms conversion time
  }
  celsius = (float)raw / 16.0;
  return celsius;
}

 
void loop(void) {
  ispeople=digitalRead(peoplePin);

  if(ispeople)        //如果有人通
    digitalWrite(innerLed,HIGH);       //发光模块点亮
  else
    digitalWrite(innerLed,LOW);       //发光模块熄灭

  // 花盆组织逻辑
  soilValue=analogRead(soilPin);
  lightValue=analogRead(lightPin);
  knobValue=analogRead(knobPin);

/*debug
  Serial.print(soilValue);
  Serial.print(',');
  Serial.print(lightValue);
  Serial.print(',');
  Serial.print(heatValue);
  Serial.print(',');
  Serial.println(knobValue);
*/
  //大于设定的之需要补水 但不要超过一般值
  if(soilValue > knobValue ){
    digitalWrite(waterPin,1);
  }
  else{
    digitalWrite(waterPin,0);
  }

  //todo sound light
  if(soundValue > knobValue ){
    digitalWrite(waterPin,1);
  }



  // 串口数据交换
  if(Serial.available()>0){
    char in = Serial.read();
    switch(in){
      case 'l':
      Serial.println(lightValue);
      break;
      case 'h':
      heatValue=getTemplate();
      if(heatValue!=0.0)
        Serial.println(heatValue);
      
      break;
      case 'k':
      Serial.println(knobValue);
      break;
       
      case 's':
      Serial.println(soilValue);
      break;

      case 'p':
      Serial.println(ispeople);
      break;
      case 'v':
      Serial.println('0');
      
      default:
      break;
    }
  }

}
