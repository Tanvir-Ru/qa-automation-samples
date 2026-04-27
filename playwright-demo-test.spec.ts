// playwright-demo-test.spec.ts
// A simple Playwright test for SauceDemo (public demo site)
// Run with: npx playwright test

import { test, expect } from '@playwright/test';

test.describe('SauceDemo Login and Purchase Flow', () => {
  
  test('User can login, add item to cart, and checkout', async ({ page }) => {
    // Navigate to the demo site
    await page.goto('https://www.saucedemo.com/');
    
    // Login with standard user
    await page.fill('[data-test="username"]', 'standard_user');
    await page.fill('[data-test="password"]', 'secret_sauce');
    await page.click('[data-test="login-button"]');
    
    // Verify login success by checking inventory page loads
    await expect(page).toHaveURL(/inventory.html/);
    await expect(page.locator('[data-test="inventory-container"]')).toBeVisible();
    
    // Add backpack to cart
    await page.click('[data-test="add-to-cart-sauce-labs-backpack"]');
    
    // Go to cart
    await page.click('[data-test="shopping-cart-link"]');
    await expect(page.locator('[data-test="cart-list"]')).toBeVisible();
    
    // Verify backpack is in cart
    const cartItem = page.locator('[data-test="inventory-item-name"]');
    await expect(cartItem).toHaveText('Sauce Labs Backpack');
    
    // Proceed to checkout
    await page.click('[data-test="checkout"]');
    
    // Fill checkout information
    await page.fill('[data-test="firstName"]', 'Test');
    await page.fill('[data-test="lastName"]', 'User');
    await page.fill('[data-test="postalCode"]', '12345');
    await page.click('[data-test="continue"]');
    
    // Verify checkout overview page
    await expect(page.locator('[data-test="checkout-summary-container"]')).toBeVisible();
    
    // Finish checkout
    await page.click('[data-test="finish"]');
    
    // Verify order complete
    const completeHeader = page.locator('[data-test="complete-header"]');
    await expect(completeHeader).toHaveText('Thank you for your order!');
  });
  
  test('User sees error message with invalid password', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    
    // Try invalid login
    await page.fill('[data-test="username"]', 'standard_user');
    await page.fill('[data-test="password"]', 'wrong-password');
    await page.click('[data-test="login-button"]');
    
    // Verify error message appears
    const errorMessage = page.locator('[data-test="error"]');
    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toContainText('Username and password do not match');
  });
});
