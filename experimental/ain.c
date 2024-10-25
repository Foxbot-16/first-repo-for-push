uint8_t  DEBOUNCE_CHECK = 0 ;
uint32_t  DEBOUNCE_COUNT = 0 ;

/* USER CODE END PV */



/* USER CODE BEGIN SysTick_IRQn 1 */

  if(DEBOUNCE_CHECK)
  {
	  //let's wait a bit (30ms)
	  if(DEBOUNCE_COUNT >= DEBOUNCE_TIME)
	  {
		  //let's check if it's a bug or a success
		  if(LL_GPIO_IsInputPinSet(GPIOC, LL_GPIO_PIN_13))
		  {
			// if it's a success turn the led on
			LL_GPIO_TogglePin(GPIOA, LL_GPIO_PIN_5);
		  }
		  
		  // set to zero both variables
		  // either it was a success or a bug 
		  DEBOUNCE_COUNT = 0 ;
		  DEBOUNCE_CHECK = 0 ;

	  }
	  DEBOUNCE_COUNT++;
  }
  /* USER CODE END SysTick_IRQn 1 */