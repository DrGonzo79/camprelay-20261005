import {test,expect} from "@playwright/test";
test("parent filters, queues a primary and backup, and arms the relay",async({page})=>{
 await page.goto("/");
 await expect(page.getByRole("heading",{name:/Build the camp plan/i})).toBeVisible();
 await expect(page.getByText("3 matching fictional camps")).toBeVisible();
 await page.getByRole("button",{name:/Add to relay/}).nth(0).click();
 await page.getByRole("button",{name:/Add to relay/}).nth(0).click();
 await expect(page.getByText("2/3 added to relay")).toBeVisible();
 await page.getByRole("button",{name:"Arm demo monitor"}).click();
 await expect(page.getByText("Your relay is registration-ready.")).toBeVisible();
 await expect(page.getByText(/At opening: alert parent/)).toBeVisible();
});
test("empty and validation states are clear",async({page})=>{
 await page.goto("/");
 await page.getByLabel("Search camps").fill("no-such-camp");
 await expect(page.getByText("No camps match this brief")).toBeVisible();
 await page.getByRole("button",{name:"Reset"}).click();
 await page.getByRole("button",{name:/Add to relay/}).first().click();
 await page.getByRole("button",{name:"Arm demo monitor"}).click();
 await expect(page.locator(".error")).toContainText("primary camp and at least one backup");
});
test("queue limit and mobile overflow are handled",async({page},testInfo)=>{
 await page.goto("/");
 await page.getByLabel("Require aftercare").uncheck();
 const add=page.getByRole("button",{name:/Add to relay/});
 await add.nth(0).click();await add.nth(0).click();await add.nth(0).click();
 await page.getByRole("button",{name:/Add to relay/}).first().click();
 await expect(page.locator(".error")).toContainText("at most three camps");
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
 expect(overflow).toBeLessThanOrEqual(1);
 await page.screenshot({path:testInfo.outputPath("camprelay.png"),fullPage:true});
});
